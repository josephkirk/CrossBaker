import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.11
Item {
    property var textColor: "white"
    height: 60
    ColumnLayout {            
        anchors.fill: parent
        // padding: 5
        RowLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.alignment: Qt.AlignLeft
            Label { 
                text: '<b>App Name:</b> '
                color:textColor
                font.pointSize: 10
            }
            Text {
                text: model.modelData.appname
                font.pointSize: 12
                color:textColor
                }
        }
        RowLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.alignment: Qt.AlignLeft
            Label {
                text: '<b>Path:</b>'
                color:textColor
                font.pointSize: 10
            }
            TextField {
                id: apppathedit
                Layout.fillWidth: true
                text: model.modelData.apppath
                verticalAlignment : TextInput.AlignBottom
                color:textColor
                font.pointSize: 8
                onEditingFinished: {
                    model.modelData.apppath = apppathedit.text
                    console.log("change Path to "+ model.modelData.apppath)
                }
            }
        }
    }
}