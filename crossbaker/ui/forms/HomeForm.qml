import QtQuick 2.11
import QtQuick.Controls 1.4
import QtQuick.Controls 2.4
import QtQml.Models 2.11
import "stylings"

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
    header: Rectangle {
        height: 50
        gradient: clubcolors
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
                    color: "white"
                    anchors.verticalCenter: parent.verticalCenter
                    text: name
                    font.pixelSize: 14
                }
            }
        }
    }

    Rectangle {
        color: "#F0F0DF"
        width: parent.width
        height: parent.height
        ListView {
            id: layerview
            anchors.fill: parent.fill
            width: parent.width
            height: parent.height
            spacing: 5
            y: 10
            // header: bannercomponent
            // headerPositioning: ListView.PullBackHeader
            // footer: footercomponent
            // footerPositioning: ListView.PullBackFooter

            Component.onCompleted: {
                model = visualModel
                // console.log(layerModel)
            }
        }
    }

    footer: Rectangle {
        height: 100
        color: "#423C40"
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
