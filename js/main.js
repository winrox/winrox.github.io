_.templateSettings = {
  interpolate: /\{\{(.+?)\}\}/g /*Lets you use {{}} for templating instead of <%= %>*/
};

var Photo = Backbone.Model.extend({
  defaults:{
    imageSource: "",
    alternativeText: "",
    className: "center-text",
    cssId:"",
    category: ""
  }
});


/*-----------------------------------------------------*/
var photo = new Photo;

photo.attributes.category = "drawing";

photo.attributes.imageSource = "img/art/ace.jpg";

photo.attributes.alternativeText = "still-life drawing of a bottle, and ace card, and a koosh ball";
/*-----------------------------------------------------*/

var Photos = Backbone.Collection.extend({
  model: Photo
  //url: "/api/photos"
});

var photos = new Photos([
  new Photo({imageSource: "img/art/abstractsands.jpg", cssId: "first-photo", alternativeText: "a colorful abstract drawing that could be be seen as layers of sand", className: "center-text", category: "drawing"}),
  new Photo({imageSource: "img/art/bluesquirrel.jpg", alternativeText: "a bright blue squirrel painting", className: "center-text", category: "painting"}),
  new Photo({imageSource: "img/art/littlebluebirdonbranchabstract.jpg", cssId: "little-blue-bird", alternativeText: "colorful painting with a small blue bird on a branch", className: "center-text", category: "painting" })
]);

var my_template = _.template('<div class="item"><img src="{{imageSource}}" alt="{{alternativeText}}" id="{{cssId}}" class="{{className}}"></div>'); //<div class="item"><img id="{{cssId}}" src="{{imageSource}}" alt="{{alternativeText}}" class=("item "+"{{className}}")></div>


var PhotoView = Backbone.View.extend({

  initialize: function(){
    // this.render();
  },

  // render: function(){
  //   $('#photos-view').html(my_template(photo.toJSON()));
  // }

  render: function(){
  this.$el.attr("id", this.model.id);
  this.$el.html(my_template(this.model.toJSON()));

  return this;
}

});

// var photoView = new PhotoView ({ el: "#photos-view", model: photo });
// photoView.render();

var PhotosView = Backbone.View.extend({
  initialize: function(){
    // this.render();
  },

  // render: function(){
  //   var photosToRender;
  //   for(var i = 0; i < photos.find().collection.length; i++){
  //     if(i == photos.find().collection.length-1){
  //       photosToRender += 'my_template(photos.find()collection.models[i].toJSON())';
  //     }
  //     photosToRender += 'my_template(photos.find()collection.models[i].toJSON()) +';
  //   }
  //   return $('#photos-view').html(photosToRender);
  // }

  render: function(){
    var self = this;

    if (this.model)
      //below renders the registration number from the model, grabbing it from each vehicle
      //this.$("#newVehiclediv").html(this.model.get("registrationNumber")); // not sure what this is supposed to do

    this.model.each(function(photo){

      var photoView = new PhotoView({ el: "#photos-view", model: photo });
      console.log("about to render " + photo.attributes.imageSource);
      self.$el.append(my_template(photo.toJSON()));
      console.log("rendered " + photo.attributes.imageSource);

    });
    $('#photos-view').children()[0].className = "item active";
    console.log("first slide active");
  }

});

var photosView = new PhotosView({ el: "#photos-view", model: photos });
//photosView.render();

$( document ).ready(photosView.render());

/*______---------BEGINS GAMES______------_________---------_________------!!!!*/

var Game = Backbone.Model.extend({
  defaults:{
    name: "",
    source: ""
  }
});

var game = new Game([
  new Game({ name: "tic tac toe", source: "www.artbywinnie.com/tic_tac_toe/" })
]);

var Games = Backbone.Collection.extend({
  model: Game
});

var games = new Games([
  new Game({ name: "tic tac toe", source: "www.artbywinnie.com/tic_tac_toe/" })
]);

var game_template = _.template('<iframe id="gameIframe" src="http://www.artbywinnie.com/tic_tac_toe/"></iframe>');

var GameView = Backbone.View.extend({

  initialize: function(){
  },


  render: function(){
  this.$el.attr("id", this.model.id);
  this.$el.html(game_template(this.model.toJSON()));
  console.log(this.$el.html(game_template(this.model.toJSON())));

  return this;
}

});

var gameView = new GameView ({ el: "#game-view", model: game });

function revealTicTacToe(){
  gameView.render();
  $("#tttBtn").hide();
}
