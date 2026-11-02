# Language structure

English is the default edition at `https://ai.qu3vipon.com/`. Korean is published at `https://ai.qu3vipon.com/ko/`.

| Source | Purpose |
| --- | --- |
| `docs/en/` | English pages matching all Korean paths; introductions, prerequisites, and LLM chapters translated; FastAPI drafts remain pending |
| `docs/ko/` | Existing Korean Markdown, including unpublished chapters |
| `docs/assets/` | Shared images |
| `docs/stylesheets/` | Shared styles |
| `zensical.toml` | English navigation, metadata, and UI language |
| `zensical.ko.toml` | Korean navigation, metadata, and UI language |
| `scripts/site.py` | Shared-resource preparation and combined build |

Both editions use Zensical's native `theme.language` and `extra.alternate` language selector. Zensical does not currently provide an integrated content-translation pipeline; each edition is built separately. No third-party i18n plugin is required. See the [official language documentation](https://zensical.org/docs/setup/language/).

## Authoring translations

Use the same Markdown path and explicit heading IDs in both editions, for example `docs/en/llm/01-machine-learning.md` and `docs/ko/llm/01-machine-learning.md`. English navigation already mirrors the Korean navigation. When a translation is ready, replace the empty body and remove `translation_pending`, `robots: noindex, follow`, and `search.exclude` from its front matter. Keep WIP chapters excluded from search engines until publication. Do not copy Korean text into English pages as an implicit fallback.

Keep relative image links unchanged. The preparation command copies shared images and styles into each edition's ignored resource directories. Edit their sources in `docs/assets/` and `docs/stylesheets/`, never the generated copies. Images containing Korean text will need English variants as their chapters are translated.

Navigation, site metadata, and palette labels are intentionally language-specific. Theme features, Markdown extensions, analytics, and asset settings should remain consistent between the two configurations.

The native language-selector UI is extended in `overrides/partials/alternate.html` to retain the current document path. Both editions must contain matching paths. `overrides/main.html` also maps the head alternate links to the corresponding documents.

## Build and preview

```sh
python scripts/site.py build
python scripts/site.py serve --port 8000
```

The preview serves both editions and their language selector on one host. It builds once at startup; restart it after editing. For live editing of one edition, prepare the resources first, then run `zensical serve -f zensical.toml` or `zensical serve -f zensical.ko.toml`.

The combined build writes English to `site/`, Korean to `site/ko/`, and combines both sitemaps at `site/sitemap.xml`. WIP pages retain their `noindex` metadata and are excluded from the sitemaps. GitHub Pages uploads the combined `site/` directory.

`overrides/404.html` generates the English error page at `site/404.html`, which GitHub Pages serves for missing URLs, including nested paths. The combined local preview uses the same page and returns HTTP 404. Its home links use absolute paths so they work from any missing URL. Existing English placeholder pages remain valid pages and do not return 404.

Untranslated English pages contain metadata only (or a coming-soon notice for WIP chapters) and are excluded from site search, search engines, and sitemaps. Completed translations have these exclusions removed. The existing unprefixed URLs now belong to the English edition; they cannot also redirect to Korean. The Korean content remains accessible at the matching `/ko/` URLs. Do not publish the empty English edition as a completed translation.
