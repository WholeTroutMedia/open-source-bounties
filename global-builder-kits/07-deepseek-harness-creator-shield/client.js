/**
 * @inception/agent-shield-sdk : client.js
 * DeepSeek Harness Browser Client UI Slot Plugin
 *
 * Injects the Inception Agent Shield status badge & x402 tier selector
 * into the DSH conversation composer dock slot.
 */

if (typeof window !== 'undefined' && window.__ModuleLoader__) {
  window.__ModuleLoader__.load({
    id: '@inception/agent-shield-sdk',
    factory(require) {
      const React = (typeof window !== 'undefined' && window.React) || require('react');
      const h = React.createElement;

      function ShieldBadge() {
        return h(
          'div',
          {
            className: 'inception-agent-shield-dock-badge',
            title: 'Inception Agent Shield V8.0 : Ashburn 3.5ms Default GPS & x402 Security Gate Active',
            style: {
              display: 'inline-flex',
              alignItems: 'center',
              gap: '6px',
              padding: '2px 8px',
              borderRadius: '9999px',
              fontSize: '11px',
              fontWeight: 600,
              fontFamily: 'ui-monospace, SFMono-Regular, Menlo, monospace',
              background: 'rgba(0, 229, 255, 0.08)',
              color: '#00e5ff',
              border: '1px solid rgba(0, 229, 255, 0.28)',
              boxShadow: '0 0 10px rgba(0, 229, 255, 0.12)',
              cursor: 'pointer',
              userSelect: 'none',
              transition: 'all 0.15s ease',
            },
          },
          h(
            'svg',
            {
              viewBox: '0 0 24 24',
              width: 14,
              height: 14,
              fill: 'none',
              stroke: '#00e5ff',
              strokeWidth: 2,
              strokeLinecap: 'round',
              strokeLinejoin: 'round',
            },
            h('path', { d: 'M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z' }),
            h('path', { d: 'm9 12 2 2 4-4' })
          ),
          h('span', null, 'CITADEL SHIELD'),
          h(
            'span',
            {
              style: {
                background: '#10b981',
                color: '#000',
                padding: '1px 5px',
                borderRadius: '6px',
                fontSize: '9px',
                letterSpacing: '0.04em',
              },
            },
            '3.5ms'
          )
        );
      }

      return {
        inject: ['slots'],
        apply(ctx) {
          if (ctx && ctx.slots && typeof ctx.slots.inject === 'function') {
            ctx.slots.inject('conversation.composer.dock', () =>
              ctx.slots.register(
                {
                  name: 'conversation.composer.dock',
                  id: 'inception-agent-shield-badge',
                  order: 10,
                },
                ShieldBadge
              )
            );
          }
        },
      };
    },
  });
}
