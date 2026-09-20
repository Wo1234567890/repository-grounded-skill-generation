# Offscreen Content Loading with User Notification Evidence

- family: 未分类技能
- skill_id: 0dc23948-d5f4-513f-a222-b90226239e27
- support_count: 2

## Evidence 1

- support_id: d1bcebb0-bb42-569d-a04e-9d3feccdb723
- relation_type: support
- document: cls-guidance.md
- doc_id: 0551d67e-cae4-5d1f-804a-e4046e4b8739
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/cls-guidance.md
- section: Common causes of CLS
- span: 25126:26410
- confidence: 0.80
- quote: In some cases adding content dynamically is an important part of user experience. For example, when loading more products to a list of items or when updating live feed content. There are several ways to avoid unexpected layout shifts in those cases:

- Replace the old content with the new content within a fixed size container or use a carousel and remove the old content after the transition. Remember to disable any links and controls until the transition has completed to prevent accidental clicks or taps while the new content is coming in.

- Have the user initiate the load of new content, so they are not surprised by the shift (for example with a "Load more" or "Refresh" button). It's recommended to prefetch the content before the user interaction so that it shows up immediately. As a reminder, layout shifts that occur within 500 milliseconds of user input are not counted towards CLS.

- Seamlessly load the content offscreen and overlay a notice to the user that it's available (for example, with a "Scroll to top" button).

Examples of dynamic content loading without causing unexpected layout shifts. Left: Live feed content loading on Twitter. Right: "Load More" example on Chloé website. Check out how the YNAP team optimized for CLS when loading more content.

## Evidence 2

- support_id: 21f3a224-d5b3-5de4-9df2-f11dacc71a53
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Integrations
- span: 15110:15729
- confidence: 0.72
- quote: SwarmZero AI
Track and analyze SwarmZero agents with full observability. Set an `AGENTOPS_API_KEY` in your environment and initialize AgentOps to get started.

- [SwarmZero](https://swarmzero.ai) - Advanced multi-agent framework
- [AgentOps integration example](https://docs.agentops.ai/v1/integrations/swarmzero)
- [SwarmZero AI integration example](https://docs.swarmzero.ai/examples/ai-agents/build-and-monitor-a-web-search-agent)
- [SwarmZero AI - AgentOps documentation](https://docs.swarmzero.ai/sdk/observability/agentops)
- [Official SwarmZero Python SDK](https://github.com/swarmzero/swarmzero)

Installation
