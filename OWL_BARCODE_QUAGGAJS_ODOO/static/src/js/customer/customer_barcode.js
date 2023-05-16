/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Layout } from "@web/views/layout";
import { KeepLast } from "@web/core/utils/concurrency";
import { Model, useModel } from "@web/views/helpers/model";
const { useRef } = owl.hooks
var rpc = require('web.rpc');



class VeryBasicModel extends Model {
    static services = ["orm"];
    constructor() {
        super(...arguments);

    }
    setup(params, { orm }) {
        this.model = params.resModel;
        this.orm = orm;
        this.keepLast = new KeepLast();
    }

    async load(params) {
        console.log(params, this.orm)
        this.data = await this.keepLast.add(
            this.orm.searchRead(this.model, params.domain, [], { limit: 1 })
        );
        this.notify();
    }
}
VeryBasicModel.services = ["orm"];

class VeryBasicView extends owl.Component {

    inputRef = useRef("input");
    focusInput() {
        this.inputRef.el.focus();
        console.log(Quagga)
    }
    constructor() {
        super(...arguments);


    }

    async mounted() {


        console.log('model', this.model)
        console.log(rpc)
        this.startScanner()
    }
    startScanner() {
        Quagga.init({
            inputStream: {
                name: "Live",
                type: "LiveStream",
                target: this.inputRef.el,
                constraints: {
                    width: 800,
                    height: 600,
                    facingMode: "environment"
                },
            },
            area: { // defines rectangle of the detection/localization area
                top: "0%",    // top offset
                right: "0%",  // right offset
                left: "0%",   // left offset
                bottom: "0%"  // bottom offset
            },
            decoder: {
                readers: [
                    "code_128_reader",
                    "ean_reader",
                    "ean_8_reader",
                    "code_39_reader",
                    "code_39_vin_reader",
                    "codabar_reader",
                    "upc_reader",
                    "upc_e_reader",
                    "i2of5_reader"
                ],
                debug: {
                    showCanvas: true,
                    showPatches: true,
                    showFoundPatches: true,
                    showSkeleton: true,
                    showLabels: true,
                    showPatchLabels: true,
                    showRemainingPatchLabels: true,
                    boxFromPatches: {
                        showTransformed: true,
                        showTransformedBox: true,
                        showBB: true
                    }
                }
            },

        }, function (err) {
            if (err) {
                console.log(err);
                return
            }

            console.log("Initialization finished. Ready to start");
            Quagga.start();

            // Set flag to is running

        });

        Quagga.onProcessed(function (result) {
            var drawingCtx = Quagga.canvas.ctx.overlay,
                drawingCanvas = Quagga.canvas.dom.overlay;

            if (result) {
                if (result.boxes) {
                    drawingCtx.clearRect(0, 0, parseInt(drawingCanvas.getAttribute("width")), parseInt(drawingCanvas.getAttribute("height")));
                    result.boxes.filter(function (box) {
                        return box !== result.box;
                    }).forEach(function (box) {
                        Quagga.ImageDebug.drawPath(box, { x: 0, y: 1 }, drawingCtx, { color: "green", lineWidth: 2 });
                    });
                }

                if (result.box) {
                    Quagga.ImageDebug.drawPath(result.box, { x: 0, y: 1 }, drawingCtx, { color: "#00F", lineWidth: 2 });
                }

                if (result.codeResult && result.codeResult.code) {
                    Quagga.ImageDebug.drawPath(result.line, { x: 'x', y: 'y' }, drawingCtx, { color: 'red', lineWidth: 3 });
                }
            }
        });

        Quagga.onDetected(function (result) {
            window.location.href = `/web#id=${result.codeResult.code}&menu_id=149&action=283&model=mrp.production&view_type=form`;
            Quagga.offProcessed();
            Quagga.offDetected();
            Quagga.stop();

            console.log("Barcode detected and processed : [" + result.codeResult.code + "]", result);
        });
    }
    onClick() {

        console.log("start")

        this.startScanner()
    }
    onStop() {
        Quagga.offProcessed();
        Quagga.offDetected();
        console.log("stop")
        Quagga.stop();

    }
    set_scannerIsRunning(bol) {
        return bol
    }

    setup() {
        this.model = useModel(VeryBasicModel, {
            resModel: this.props.resModel,
            domain: this.props.domain,
            orm: this.props.orm
        });
    }
}

VeryBasicView.type = "barcode_production_view";
VeryBasicView.display_name = "VeryBasicView";
VeryBasicView.icon = "fa-heart";
VeryBasicView.multiRecord = true;
VeryBasicView.searchMenuTypes = ["filter", "favorite"];
VeryBasicView.components = { Layout };
VeryBasicView.template = owl.tags.xml/* xml */ `
<div viewType="'barcode_production_view'" class="d-flex " style =" overflow: hidden !important;" >
<div class="d-flex justify-content-center " style="height: 70vh;top:20px">
  <div class="shadow  mb-5 mt-5 bg-white rounded " style="width: 800px; height: 600px;">
  <div t-ref="input"></div>
  </div>
</div>
<div class="d-flex justify-content-center align-items-center" style="width: 100wh; height:200px;">
<a class =" d-flex justify-content-center align-items-center bg-primary hover col-6 text-white"   t-on-click ="onClick" style="height:200px;">
<h1 class ="text-white font-weight-bold text-2xl ">SCAN</h1>
</a>
<a  class =" d-flex justify-content-center align-items-center bg-danger hover col-6 text-white"  t-on-click ="onStop" style="height:200px;">
<h1 class ="text-white font-weight-bold text-2xl ">STOP</h1>
</a>
</div>
</div>`;

registry.category("views").add("barcode_production_view", VeryBasicView);


