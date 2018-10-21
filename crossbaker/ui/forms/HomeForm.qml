import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQml.Models 2.11
import QtQuick.Layouts 1.11
import "stylings"
import "items"
Page {
    id: homepage
    title: qsTr("Set up")
    width: 400
    height: 750
    property var model
    property var baker
    property var bakers
    // Components Init
    BannerColors {
        id: clubcolors
    }
    header: PageHeader {
        Row {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter 
            Text {
                color: "white"
                font.bold: true
                font.pixelSize: 20
                text: "Baking Group"
            }
        }
    }

    // Body
    DelegateModel {
        id: visualModel
        model: ListModel {
            ListElement { name: "Bake Group 1" }
            ListElement { name: "Bake Group 2" }
        }
        delegate: Rectangle {
            height: 50
            width: parent.width-20
            color: "#3F5866"
            x: 10
            radius: 5
            Row {
                anchors.verticalCenter: parent.verticalCenter 
                spacing: 10
                padding: 10
                Rectangle {
                    radius: 5
                    width: 40
                    height: 40
                    color: "#BDD3DE"
                }
                Text { 
                    color: "black"
                    anchors.verticalCenter: parent.verticalCenter
                    text: name
                    font.pixelSize: 14
                }
            }
        }
    }

    PageBody {
        ListView {
            x: 5; y: 10
            width: parent.width; height: 600
            spacing: 5
            Component.onCompleted: {
                model = visualModel
                // console.log(layerModel)
            }
        }
    }

    footer: PageFooter {
        Row {
            spacing: 10
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter           
            ComboBox {
                // anchors.verticalCenter: parent.verticalCenter
                width: 200
                model: bakers
            }
            Button {
                width: 150
                text: "Run Baker"
                onClicked: baker.run()
            }
        }
    }
}
