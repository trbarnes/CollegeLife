var app = new Vue({
  el: '#app',
  data: {
    suggestions: [],
    seen:true,
    unseen:false
  },
  //Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
  created: function() {
        this.fetchSuggestionList();
        this.timer = setInterval(this.fetchSuggestionList, 10000);
  },
  methods: {
    fetchSuggestionList: function() {
        // $.get('/suggestions/', function(suggest_list) {
        //     this.suggestions = suggest_list.suggestions;
        //     console.log(suggest_list);
        // }.bind(this));
        axios
          .get('/suggestions/')
          .then(response => (this.suggestions = response.data.suggestions))
        console.log(this.suggestions)
    },
    cancelAutoUpdate: function() { clearInterval(this.timer) }
  },
  beforeDestroy() {
    clearInterval(this.timer)
  }

})
