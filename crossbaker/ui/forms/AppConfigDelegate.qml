import QtQuick 2.11
import QtQuick.Controls 2.4

Component {
    Item {
        width: 180
        height: 100
        Column {
            spacing: 5
            Row {
                spacing: 5
                Label { text: '<b>App Name:</b> '}
                TextField { placeholderText: name }
            }
            Row {
                spacing: 5
                Label { text: '<b>Path:</b>'}
                TextField { placeholderText: number }
            }
        }
    }
}