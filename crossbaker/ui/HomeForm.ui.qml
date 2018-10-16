import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Controls 1.4
import Qt.labs.folderlistmodel 2.11
import QtQml.Models 2.11
Page {
    id: homePage
    title: qsTr("Home")
    width: 400
    height: 800

    TreeView {
        id: objectview
        anchors.fill: parent
        model: assetModel
        selection: ItemSelectionModel {
            model: assetModel
        }
        TableViewColumn {
            title: "Name"
            role: "name"
        }
    }
}
