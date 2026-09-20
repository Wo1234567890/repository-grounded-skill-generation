# Monitor Live CLS During User Interaction Evidence

- family: 未分类技能
- skill_id: 4cf1f416-b910-53e6-9cd4-08ea9a9bf8f0
- support_count: 2

## Evidence 1

- support_id: 9d0398e3-b201-5e1e-b1c9-fdfea5b659bc
- relation_type: support
- document: cls-guidance.md
- doc_id: 0551d67e-cae4-5d1f-804a-e4046e4b8739
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/cls-guidance.md
- section: Understand the causes of layout shifts
- span: 7817:12731
- confidence: 0.82
- quote: Before you start looking at solutions to common CLS issues, it's important to understand your CLS score and where the shifts are coming from.

CrUX is the Google dataset of the Web Vitals program, and for that, CLS is measured throughout the full life of the page and not just during the initial page load that lab tools typically measure.

PageSpeed Insights shows both the user-perceived
CLS from a URL in its "Discover what your real users are experiencing" section,
and the lab-based load CLS in its "Diagnose performance issues" section.
Differences between these values are likely the result of post-load CLS.

In this example, CrUX measures a much larger CLS than Lighthouse.

Lighthouse's detailed CLS diagnostics.

The Performance panel in DevTools provides a wealth of information on layout shifts:

After recording a new trace in the Performance panel, the Layout Shifts track of the results is populated with purple bars displaying a `Layout Shift` clusters. Clicking the diamonds shows an animation of the shift and details in the Summary panel.

Layout shifts are highlighted in the Layout shifts track. The purple line groups shifts into shift clusters with the diamonds showing individual shifts in that cluster. The size of the diamond is proportional to the size of the shift allowing you to hone in on the largest shifts.

Clicking on a shift shows a pop up with an animation of the shift and highlights the elements shift in purple.

Additionally, the Summary view for a `Layout Shift` record includes the start time, the shift score as well as the elements shifted. This is particularly helpful to get more detail on load CLS issues since this is easily replicated with a reload performance profile.

This also links to the Layout shift culprits insight displayed in the Insights panel on the left, which shows the total CLS at the top, as well as possible reasons for layout shifts.

Identify post-load CLS issues
Disagreement between the CrUX and Lighthouse CLS scores often indicates post-load CLS. These shifts can be tricky to track down without field data. For information on collecting field data, see Measure CLS elements in the field.

The live metrics view of the Performance Panel lets you interact with the page and monitor the CLS score to identify interactions causing large layout shfts.

## Evidence 2

- support_id: 2d84cb84-ecd0-5af4-93d2-000faa0af9ab
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 20407:20724
- confidence: 0.90
- quote: Before starting work on a new feature:
   ```bash
   git checkout main
   git pull upstream main
   git checkout -b feature/your-feature-name
   ```

2. **Install Dependencies**:
   ```bash
   pip install -e .
   ```

3. **Set Up Pre-commit Hooks**:
   ```bash
   pre-commit install
   ```

## Development Environment
