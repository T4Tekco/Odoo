/** @odoo-module **/

import public_widget from "web.public.widget";

export default public_widget.registry.t4_contact_searchbar =
  public_widget.Widget.extend({
    selector: ".t4_search_form",
    /**
     * @override
     */
    start: function () {
      let _form = this.el;

      window.v_form = _form;
      console.log(_form);
    },
  });
