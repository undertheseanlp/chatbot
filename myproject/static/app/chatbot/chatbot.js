app.controller("ChatbotCtrl", function ($scope) {
  $scope.sentences = [];
  $scope.showMessage = ChatbotConfiguration.showMessage;
  console.log($scope.showMessage);
  function generateUUID() { // Public Domain/MIT
    var d = new Date().getTime();
    if (typeof performance !== 'undefined' && typeof performance.now === 'function'){
        d += performance.now(); //use high-precision timer if available
    }
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = (d + Math.random() * 16) % 16 | 0;
        d = Math.floor(d / 16);
        return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
}
  $scope.init = function(){
    console.log("Chào bạn. Hehe");
    var uid;
    // load or create new session
    if(!localStorage.getItem("uid")){
      uid = generateUUID();
      localStorage.setItem("uid", uid);
    }
    uid = localStorage.getItem("uid");
    console.log(uid);
    $scope.uid = uid;

  };

  $scope.init();
  $scope.suggestion = "gõ gì đó đi mà...";
  $scope.state = "init";
  $scope.addTalk = function () {
    var message = $scope.userText;
    $scope.talk("you", message);
    $scope.reply(message);

  };

  $scope.reply = function (message) {
    $.ajax({
      type: "POST",
      url: "./chatbot",
      data: JSON.stringify({"text": message, "uid": $scope.uid}),
      contentType: 'application/json'
    }).done(function (data) {
      try {
        var text = data["output"];
        $scope.sentences.push(
          {"agent": "bot", "text": text}
        );
        $scope.$apply();
        $scope.afterTalk();
        // $scope.talk("bot", text);
      } catch (e) {
        console.log("Cannot get reply from bot.");
      }
    });
  };
  $scope.talk = function (agent, text) {
    $scope.sentences.push(
      {"agent": agent, "text": text}
    );
    console.log(agent, text);
    $scope.afterTalk();
  };


  $scope.afterTalk = function () {
    $scope.updateState();
    $scope.updateSuggestion();
    setTimeout(function () {
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
