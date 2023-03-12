odoo.define("t4_grapesjs.t4_grapesjs", function (require) {
  "use strict";

  let public_widget = require("web.public.widget");

  public_widget.registry.t4_grapesjs = public_widget.Widget.extend({
    selector: "#t4_grapesjs",
    /**
     * @override
     */
    start: function () {
      let root = this.el;
      let input_css = root.querySelector("#t4_form_css");
      let input_body = root.querySelector("#t4_form_body");

      let editor_element = root.querySelector("#t4_grapesjs_editor");

      editor_element.innerHTML = input_body.value;

      let editor = grapesjs.init({
        container: editor_element,
        fromElement: true,
        showOffsets: true,
        storageManager: false,
        plugins: [
          "gjs-blocks-basic",
          "grapesjs-plugin-forms",
          "grapesjs-component-countdown",
          "grapesjs-plugin-export",
          "grapesjs-tabs",
          "grapesjs-custom-code",
          "grapesjs-touch",
          "grapesjs-parser-postcss",
          "grapesjs-tooltip",
          "grapesjs-tui-image-editor",
          "grapesjs-typed",
          "grapesjs-style-bg",
          "grapesjs-preset-webpage",
        ],
        pluginsOpts: {
          "gjs-blocks-basic": { flexGrid: true },
          "grapesjs-tabs": {
            tabsBlock: { category: "Extra" },
          },
          "grapesjs-tabs": {
            tabsBlock: { category: "Extra" },
          },
          "grapesjs-preset-webpage": {
            modalImportTitle: "Import Template",
            modalImportLabel:
              '<div style="margin-bottom: 10px; font-size: 13px;">Paste here your HTML/CSS and click Import</div>',
            modalImportContent: function (editor) {
              return (
                editor.getHtml() + "<style>" + editor.getCss() + "</style>"
              );
            },
          },
        },
      });

      editor.setStyle(input_css.value);

      editor.on("update", () => {
        input_css.value = editor.getCss();
        input_body.value = editor.getHtml();
      });
    },
  });

  return public_widget.registry.t4_grapesjs;
});
