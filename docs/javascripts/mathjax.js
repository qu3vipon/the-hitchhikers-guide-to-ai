window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
};

document$.subscribe(() => {
  if (window.MathJax.startup?.promise) {
    window.MathJax.startup.promise.then(() => {
      window.MathJax.typesetClear();
      return window.MathJax.typesetPromise();
    });
  }
});
