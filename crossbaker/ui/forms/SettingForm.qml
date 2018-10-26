import QtQuick 2.11
import QtQuick.Controls 2.4
import "items"
import "delegates"
Page {
    id: configpage
    title: qsTr("Setting")
    width: 400
    height: 750
    property var settings: undefined

    header: PageHeader {
        Row {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter 
            Text {
                text: qsTr("Bake Setting")
                font.pixelSize: 24
                color: "white"
            }
        }
    }

    // Body
    PageBody {
        ListView {
            x: 5; y: 10
            width: 600; height: 600
            spacing: 5
            delegate: AppConfigDelegate {
                textColor:"black"
                width: 600
            }
            populate: Transition {
                SequentialAnimation {
                    id: popTrans
                    PauseAnimation {
                        duration: (popTrans.ViewTransition.targetIndexes * 20)
                        }
                        NumberAnimation { property: "opacity"; from: 0; to: 1.0; duration: 150 }
                        NumberAnimation { 
                            properties: "y"; duration: 150;
                            easing.type: Easing.InOutQuad; }
                    }
            }

            Component.onCompleted: {
                // Delay load model for animation
                if (settings != undefined) {
                    model = settings
                }
            }
        }
    }

    footer: PageFooter {
        Row {
            spacing: 10
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter      
            Button {
                width: 150
                text: "Save Settings"
                onClicked: {
                    console.log(Settings)
                }
            }
        }
    }
    // Styling
    
}
