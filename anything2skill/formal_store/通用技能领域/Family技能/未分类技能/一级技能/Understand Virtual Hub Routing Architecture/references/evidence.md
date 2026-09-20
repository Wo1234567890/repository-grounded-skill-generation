# Understand Virtual Hub Routing Architecture Evidence

- family: 未分类技能
- skill_id: aae37de2-0fde-500b-bd48-9d2629ad8a2a
- support_count: 2

## Evidence 1

- support_id: afddbda9-3c71-59f8-b166-03e99073e56a
- relation_type: support
- document: azure-virtual-wan-docs.md
- doc_id: 3937f901-1162-503e-8dde-3cd1a710796b
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/azure-virtual-wan-docs.md
- section: # About virtual hub routing
- span: 1263:1870
- confidence: 0.70
- quote: ## 
 In this article

The routing capabilities in a virtual hub are provided by a router that manages all routing between gateways using Border Gateway Protocol (BGP). A virtual hub can contain multiple gateways such as a Site-to-site VPN gateway, ExpressRoute gateway, Point-to-site gateway, Azure Firewall. This router also provides transit connectivity between virtual networks that connect to a virtual hub and can support up to an aggregate throughput of 50 Gbps. These routing capabilities apply to Standard Virtual WAN customers.

To configure routing, see How to configure virtual hub routing.

## Evidence 2

- support_id: fd92f780-786e-56a9-8650-d26bf2bfa9db
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Integrations
- span: 7171:7561
- confidence: 0.80
- quote: for event in stream:
    if event.event_type == "text-generation":
        print(event.text, end='')

agentops.end_session('Success')
```

Anthropic
Track agents built with the Anthropic Python SDK (>=0.32.0).

- [AgentOps integration guide](https://docs.agentops.ai/v1/integrations/anthropic)
- [Official Anthropic documentation](https://docs.anthropic.com/en/docs/welcome)

Installation
