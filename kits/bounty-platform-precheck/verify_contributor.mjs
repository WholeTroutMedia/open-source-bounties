#!/usr/bin/env node
/**
 * Zero-Knowledge Bounty Platform & Maintainer Pre-Check SDK (`verify_contributor.mjs`).
 * Includes MOAT-141/142 Split-Horizon CI Context Gate so bot operators cannot use local CLI
 * self-checks to test whether their newest probation sockpuppet accounts were caught.
 */
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const LIVE_FEED_URL =
  "https://raw.githubusercontent.com/WholeTroutMedia/open-source-bounties/main/registry/verified_spam_bot_blocklist.json";
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const LOCAL_FALLBACK = path.resolve(__dirname, "../../registry/verified_spam_bot_blocklist.json");

export async function checkGithubContributor(username, ciStrict = false) {
  const clean = String(username || "").trim().replace(/^@/, "").toLowerCase();
  const actorSha256 = crypto.createHash("sha256").update(clean, "utf8").digest("hex");
  const saltedCiSha256 = crypto
    .createHash("sha256")
    .update(`v2-ci-gate::${clean}`, "utf8")
    .digest("hex");
  const inGithubActions =
    String(process.env.GITHUB_ACTIONS || "").toLowerCase() === "true" || Boolean(ciStrict);

  let feed = null;
  if (fs.existsSync(LOCAL_FALLBACK)) {
    try {
      feed = JSON.parse(fs.readFileSync(LOCAL_FALLBACK, "utf8"));
    } catch {
      feed = null;
    }
  }
  if (!feed) {
    const resp = await fetch(LIVE_FEED_URL, {
      headers: { "User-Agent": "OSS-Bot-Shield-Precheck/2.1" },
    });
    feed = await resp.json();
  }
  const confirmed = new Set(
    (feed.blocked_actor_sha256_hashes || feed.verified_bot_handle_sha256_hashes || []).map((h) =>
      String(h).trim().toLowerCase()
    )
  );
  const probationSalted = new Set(
    (feed.probation_ci_salted_sha256_hashes || []).map((h) => String(h).trim().toLowerCase())
  );

  const isBlocked = inGithubActions
    ? confirmed.has(actorSha256) || probationSalted.has(saltedCiSha256)
    : confirmed.has(actorSha256);

  return {
    actor_sha256: actorSha256,
    actor_blinded_id: `ACTOR-SHA256-${actorSha256.slice(0, 12).toUpperCase()}`,
    is_verified_spam_bot: isBlocked,
    verification_context: inGithubActions ? "GITHUB_ACTIONS_CI_STRICT" : "PUBLIC_STANDARD_LOOKUP",
    recommended_action: isBlocked ? "REJECT_PR_AND_HOLD_BOUNTY" : "ALLOW_HUMAN_REVIEW",
    active_protection_layers: 20,
  };
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const rawArgs = process.argv.slice(2);
  const strictFlag = rawArgs.includes("--ci-strict");
  const cleanArgs = rawArgs.filter((a) => a !== "--ci-strict");
  const target = cleanArgs[0] || "human-developer";
  checkGithubContributor(target, strictFlag).then((res) => {
    console.log(JSON.stringify(res, null, 2));
    process.exit(res.is_verified_spam_bot ? 1 : 0);
  });
}
