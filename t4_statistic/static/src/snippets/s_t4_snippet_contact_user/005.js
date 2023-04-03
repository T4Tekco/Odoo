/** @odoo-module **/

import public_widget from "web.public.widget";
import {qweb} from "web.core";

export default public_widget.registry.t4_statistic = 
    public_widget.Widget.extend({
        selector: ".contact_snippet_statistics",
        start:function(){
            console.log("hello babe");
            this._rpc({
                route:"/s/usercontact",
                params: {},
            }).then((r)=>{
                console.log(r)
                this._render(r)
            });
        },

        _render:function(data) {
            let template = "t4_statistic.s_t4_statistic_contact_user"
            let output = qweb.render(template,{contact: data});
            console.log(output)
            let div = document.createElement("div")
            div.innerHTML = output;
            div.classList.add("t4_statistic_result");
            this.el.append(div);
            console.log(data);
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

        
    })