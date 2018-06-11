app.controller("ChatbotCtrl", function ($scope) {
    $scope.sentences = [
        // {"agent": "bot", "text": "chào bạn"},
    ];

    $scope.suggestion = "gõ gì đó đi mà...";
    $scope.state = "init";
    $scope.addTalk = function () {
        $scope.talk("you", $scope.userText);
    };


    $scope.talk = function (agent, text) {
        $scope.sentences.push(
            {"agent": agent, "text": text}
        );
        $scope.afterTalk();
    };


    $scope.afterTalk = function () {
        $scope.updateState();
        $scope.updateSuggestion();
        setTimeout(function(){
            $scope.updateUI();
        }, 20);

    };

    $scope.updateUI = function () {
        var dialogDom = document.getElementById("chat-dialog");
        dialogDom.scrollTop = dialogDom.scrollHeight;
    };


    $scope.updateState = function () {
         $scope.userText = "";
        if ($scope.state == "init") {
            $scope.state = "not-init";
        }
    };

    $scope.updateSuggestion = function () {
        if ($scope.state == "init") {
            $scope.suggestion = "gõ gì đó đi mà...";
        } else {
            $scope.suggestion = "viết tin nhắn của bạn...";
        }
    };
});
