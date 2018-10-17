import QtQuick 2.11
import QtQuick.Controls 1.4
import QtQuick.Controls 2.4
import QtQml.Models 2.11
Page {
    id: homepage
    title: qsTr("Set up")
    width: 400
    height: 800
    contentWidth: width
    contentHeight: height
    property var model: undefined
    property var baker: undefined
    property var json: [
        {name:"bakerGroup", ob:"low"},
        {name:"bakerGroup2", ob:"low"}
    ]
    Column {
        // leftPadding: 5
        Rectangle {
            id: bakercombo
            width: parent.width
            height: 50
            color: "gray"
            Row {
                leftPadding: 15
                spacing: 10
                Label {
                    anchors.verticalCenter: parent.verticalCenter
                    text: "Baker"
                    width: 100
                    color: "white"
                    font.bold: true
                    font.family: "san-serif"
                    font.pointSize: 16
                }
                ComboBox {
                    anchors.verticalCenter: parent.verticalCenter
                    horizontalAlignment: ComboBox.AlignRight
                    width: 200
                    model: [
                        "Marmoset",
                        "Substance",
                    ]
                }
            }
        }
        TreeView {
            id: layerview
            width: homepage.width
            height: 400
            TableViewColumn {
                title: "Title"
                role: "title"
            }

            TableViewColumn {
                title: "Description"
                role: "description"
            }
            Component.onCompleted: {
                if (model!= undefined) {
                    model:homepage.model
                }
            }
        }
        Button {
            anchors.right: parent.right
            width: 100
            text: "Run Baker"
            onClicked: baker.run()
        }
    }
}
