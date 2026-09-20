# Diagnose CLS Score Discrepancies Evidence

- family: 未分类技能
- skill_id: dff1010b-df20-5916-8391-8992ca879246
- support_count: 1

## Evidence 1

- support_id: 766c62ca-1480-5ea2-bcd9-1c4119becc88
- relation_type: support
- document: cls-guidance.md
- doc_id: 0551d67e-cae4-5d1f-804a-e4046e4b8739
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/cls-guidance.md
- section: Understand the causes of layout shifts
- span: 7817:12731
- confidence: 0.85
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
