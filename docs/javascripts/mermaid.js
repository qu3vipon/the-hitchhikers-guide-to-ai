mermaid.initialize({ startOnLoad: false });

const renderMermaidDiagrams = async () => {
  const diagrams = [...document.querySelectorAll(".mermaid")];

  diagrams.forEach((diagram) => {
    if (!diagram.dataset.source) {
      diagram.dataset.source = diagram.textContent.trim();
    }

    diagram.removeAttribute("data-processed");
    diagram.textContent = diagram.dataset.source;
  });

  const colors = getComputedStyle(document.body);
  const background = colors.getPropertyValue("--md-default-bg-color").trim();
  const theme = document.body.dataset.mdColorScheme === "slate" ? "dark" : "default";

  mermaid.initialize({
    startOnLoad: false,
    theme,
    themeVariables: {
      edgeLabelBackground: background,
    },
    themeCSS: `
      .edgeLabel, .edgeLabel * { background-color: ${background} !important; }
      .edgeLabel rect, .labelBkg { fill: ${background} !important; }
    `,
    flowchart: {
      htmlLabels: true,
    },
  });

  await mermaid.run({ querySelector: ".mermaid" });
};

document$.subscribe(() => {
  renderMermaidDiagrams();

  new MutationObserver(() => renderMermaidDiagrams()).observe(document.body, {
    attributes: true,
    attributeFilter: ["data-md-color-scheme"],
  });
});
