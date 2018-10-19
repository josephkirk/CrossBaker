import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQml.Models 2.11
import "delegates"
import "stylings"

Page {
    id: configpage
    title: qsTr("Config")
    width: 400
    height: 800
    property var appconfigs
    // Components Init
    BannerColors {
        id: clubcolors
    }

    Component {
        id: bannercomponent
        Rectangle {
            id: banner
            width: parent.width; height: 50
            gradient: clubcolors
            radius: 5
            Text {
                anchors.centerIn: parent
                text: qsTr("Application Path")
                font.pixelSize: 24
                color: "white"
            }
        }
    }

    Component {
        id: footercomponent
        Rectangle {
            id: footer
            width: parent.width
            height: 20
            gradient: clubcolors
            radius: 5
        }
    }

    // Body
    ListView {
        header: bannercomponent
        headerPositioning: ListView.PullBackHeader
        footer: footercomponent
        footerPositioning: ListView.PullBackFooter
        x: 10
        y: 10
        width: parent.width - 20
        height: parent.height - 20
        delegate: AppConfigDelegate {}

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
            model = appconfigs
        }
    }
    // Styling
}
