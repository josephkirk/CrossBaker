import QtQuick 2.11
import QtQuick.Controls 2.4
import "delegates"
Page {
    id: configpage
    title: qsTr("Config")
    width: 400
    height: 800
    contentWidth: 400
    contentHeight: 800
    Column {
        spacing: 10
        Label {
            text: qsTr("Application Path")
            anchors.horizontalCenter: parent.horizontalCenter
        }
        
        ListView {
            width: parent.width
            height: 600
            model: appmodel
            delegate: AppConfigDelegate {}
            highlight: Rectangle { color: "lightsteelblue"; radius: 2 }
        }
    }

    ListModel {
        id: appmodel
        ListElement {   
            name: "Marmoset"
            number: "marmorset.exe"
        }
        ListElement {
            name: "Substance"
            number: "sbsbaker.exe"
        }
        ListElement {
            name: "xnormal"
            number: "xnormal.exe"
        }
    }



}
