/** @odoo-module **/

import public_widget from "web.public.widget";
import { qweb } from "web.core";

export default public_widget.registry.t4_statistical =
  public_widget.Widget.extend({
        selector : ".snippet_statistics",
        start:function(){
            this._rpc({
                route: "/s/row",
                params: {},
              }).then((r) => {
                this._render(r);
              });
          
        },

        _render:function (data) {
            let template = "t4_statistic.s_t4_statistic";

            let output = qweb.render(template,{results: data});

            let div = document.createElement("div");
            div.innerHTML = output;
            div.classList.add("t4_statistic_result");
            this.el.append(div);
            console.log(data)
        },

        _cleanup: function () {
            let _form = this.el;
            let div = _form.querySelector((".t4_statistic_result"))
            if (div !== null) {
                div.remove();
                alert('No Data Sir, Try Again !');
            }
            return;
        }
    


   


  });





