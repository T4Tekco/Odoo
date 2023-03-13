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

      _form.onfocusout = () => {
        setTimeout(() => this._cleanup(), 100);
      };

      let _timeout = null;

      _input.oninput = (ev) => {
        if (_timeout != null) {
          clearTimeout(_timeout);
        }
        _timeout = setTimeout(() => this._search(ev.target.value.trim()), 1234);
      };
    },

    _search: function (query) {
      if (!query) {
        this._cleanup();
        return;
      }

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

      this._cleanup();

      // Rendered

      let output = qweb.render(template, {
        results: data,
      });
      let div = document.createElement("div");

      div.innerHTML = output;
      div.classList.add("t4_contact_result");

      _form.append(div);

      _form.classList.add("dropdown");
      _form.classList.add("show");
    },

    _cleanup: function () {
      let _form = this.el;
      _form.classList.remove("dropdown");
      _form.classList.remove("show");

      let div = _form.querySelector(".t4_contact_result");
      if (div !== null) {
        div.remove();
      }

      return;
    },
  });
