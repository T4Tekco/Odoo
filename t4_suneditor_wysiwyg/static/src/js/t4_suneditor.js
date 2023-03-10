odoo.define("t4_suneditor_wysiwyg.t4_suneditor", function (require) {
  "use strict";

  let public_widget = require("web.public.widget");

  public_widget.registry.t4_suneditor = public_widget.Widget.extend({
    selector: ".t4_suneditor",
    /**
     * @override
     */
    start: function () {
      let _input = this.el;
      let t4_editor = window.SUNEDITOR.create(_input, {
        display: "block",
        width: "100%",
        height: "auto",
        charCounter: true,
        charCounterLabel: "Characters :",
        buttonList: [
          // default
          ["undo", "redo"],
          ["font", "fontSize", "formatBlock"],
          ["paragraphStyle", "blockquote"],
          ["bold", "underline", "italic", "strike", "subscript", "superscript"],
          ["fontColor", "hiliteColor", "textStyle"],
          ["removeFormat"],
          ["outdent", "indent"],
          ["align", "horizontalRule", "list", "lineHeight"],
          ["table", "link", "image", "video", "audio"],
          ["fullScreen", "showBlocks", "codeView"],
          ["preview", "print"],
        ],
      });

      t4_editor.onChange = () => {
        _input.value = t4_editor.getContents();
      };

      return t4_editor;
    },
  });

  return public_widget.registry.t4_suneditor;
});
