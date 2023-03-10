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
      let t4_editor = window.SUNEDITOR.create(_input);

      t4_editor.onChange = () => {
        _input.value = t4_editor.getContents();
      };

      return t4_editor;
    },
  });

  return public_widget.registry.t4_suneditor;
});
