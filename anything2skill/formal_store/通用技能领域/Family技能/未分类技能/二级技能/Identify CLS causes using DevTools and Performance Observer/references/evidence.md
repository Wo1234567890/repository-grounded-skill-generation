# Identify CLS causes using DevTools and Performance Observer Evidence

- family: 未分类技能
- skill_id: c7dbc50b-9b25-5f54-9f06-fd56a3a45afe
- support_count: 2

## Evidence 1

- support_id: 9fc3bc03-dd42-5a12-b887-9b4e7b9f7100
- relation_type: support
- document: cls-guidance.md
- doc_id: 0551d67e-cae4-5d1f-804a-e4046e4b8739
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/cls-guidance.md
- section: Understand the causes of layout shifts
- span: 12737:16343
- confidence: 0.85
- quote: The live metrics view of the Performance Panel allows monitoring of a web page's CLS score while interacting with the page.

As an alternative to using the DevTools, you can browse your web page while recording layout shifts using a Performance Observer pasted into the console.

For more information, see Debug layout shifts.

After you've identified any common causes of CLS, the timespans user flow mode of Lighthouse can also be used to ensure typical user flows don't regress by introducing layout shifts.

The `web-vitals` library has attribution functions that let you collect this additional information. For more information, see Debug performance in the field. Other RUM providers have also started collecting and presenting this data similarly.

Common causes of CLS
Once you have identified the causes of CLS, you can start working on fixing the issues. In this section we will show some of the more common reasons for CLS, and what you can do to avoid them.

Images without dimensions
Always include `width` and `height` size attributes on your images and video elements. Alternatively, reserve the required space with CSS `aspect-ratio` or similar. This approach ensures that the browser can allocate the correct amount of space in the document while the image is loading.

Images without width and height specified.

Images with width and height specified.

Lighthouse 6.0 impact of setting image dimensions on CLS.

History of `width` and `height` attributes on images
In the early days of the web, developers would add `width` and `height` attributes to their `<img>` tags to ensure sufficient space was allocated on the page before the browser started fetching images. This would minimize reflow and re-layout.

```
<img src="puppy.jpg" width="640" height="360" alt="Puppy with balloons">

```

`width` and `height` in this example don't include units. These "pixel" dimensions would ensure that the browser reserved a 640x360 area in the page's layout. The image would stretch to fit this space, regardless of whether the true dimensions matched it.

When Responsive Web Design was introduced, developers began to omit `width` and `height` and started using CSS to resize images instead:

```
img {
  width: 100%; /* or max-width: 100%; */
  height: auto;
}

```

## Evidence 2

- support_id: bc895e08-c890-585e-86c1-8a6a1721d15b
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 79380:79903
- confidence: 0.65
- quote: The AgentOps dashboard provides several ways to visualize and analyze your agent's performance:

- **Session List**: Overview of all sessions with filtering options
- **Timeline View**: Chronological display of spans showing duration and relationships
- **Tree View**: Hierarchical representation of spans showing parent-child relationships
- **Message View**: Detailed view of LLM interactions with prompt and completion content
- **Analytics**: Aggregated metrics across sessions and operations

# Putting It All Together
