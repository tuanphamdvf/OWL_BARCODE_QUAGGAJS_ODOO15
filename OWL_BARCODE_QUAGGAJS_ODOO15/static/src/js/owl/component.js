const { Component } = owl;
const { xml } = owl.tags;


odoo.define('my.component', function (require) {
    "use strict";

    // Our code will be here

});
class MyComponent extends Component {
    static template = xml`
        <div class="bg-primary text-center p-3">
            Hello, World
        </div>`
}
owl.utils.whenReady().then(() => {
    const app = new MyComponent();
    app.mount(document.body);
});


