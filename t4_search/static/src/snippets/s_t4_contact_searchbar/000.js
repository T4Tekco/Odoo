/** @odoo-module **/

import public_widget from "web.public.widget";
import { qweb } from "web.core";

export default public_widget.registry.t4_contact_searchbar =
  public_widget.Widget.extend({
    selector: ".t4_search_form",
    /**
     * @override
     */
    start: function () {
      let _form = this.el;
      let _input = _form.querySelector(".t4_search_query");

      let _timeout = null;

      _input.oninput = (ev) => {
        if (_timeout != null) {
          clearTimeout(_timeout);
        }
        _timeout = setTimeout(() => this._search(ev.target.value.trim()), 2000);
      };
    },

    _search: function (query) {
      if (!query) {
        return;
      }
      console.log(query);
      this._rpc({
        route: "/s/contacts",
        params: { query: query },
      }).then((r) => {
        this._render(r);
      });
    },

    _render: function (data) {
      let _form = this.el;
      let template = "t4_search.s_t4_contact_searchbar.autocomplete";

      if (!data.length) {
        _form.classList.remove("dropdown");
        _form.classList.remove("show");
        return;
      }

      // Rendered
      console.log(data);
      console.log(_form);

      let output = qweb.render(template, {
        results: data,
      });
      let div = document.createElement("div");

      div.innerHTML = output;

      _form.append(div);

      _form.classList.add("dropdown");
      _form.classList.add("show");
    },
  });
