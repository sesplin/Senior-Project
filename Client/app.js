// import Vue from 'vue'
// import axios from 'axios'
// import VueAxios from 'vue-axios'

// Vue.use(VueAxios, axios)

var app = new Vue({
    el:"#app",
    data:{
        title: "Main Functionality",
        points: "Let's Get Points",
        pages: ["Home", "Profile", "Info"],

        server_url:"http://localhost:53454",

        cards:[],
        tcards:[],
        dcards:[],
        gcards:[],
        gascards:[],
        scards:[],
        tclicked: false,
        dclicked: false,
        gclicked: false,
        gasclicked: false,
        sclicked: false,

        new_fname:"",
        new_lname:"",
        new_email:"",
        new_pass:""

    },

    created:function(){
        this.getCards();
    },

    methods:{
        createThread: function(){
            // var for a new thread
            var new_user={
                firstName: this.new_fname,
                lastName:this.new_lname,
                email:this.new_email,
                password:this.new_pass,
            };
            //push the new thread to threads list
            fetch(this.server_url+"/newUser",{
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify(new_user)
            }).then(function(){
                //clear the inputs
                app.getCards();
                app.new_fname="";
                app.new_lname="";
                app.new_email="";
                app.new_pass="";
            })
        },

        getCards:function(){
            fetch(this.server_url+"/cards").then(function(response){
                response.json().then(function(data){
                    app.cards=data;
                    console.log(data)
                })
            })
            .catch(function(error) {
                console.log('Found error: \n', error);
              });
        },

        getTravelCards:function(){
            fetch(this.server_url+"/cards/travel").then(function(response){
                response.json().then(function(data){
                    app.tcards = data;
                    console.log(data)
                    tclicked = true
                })
            })
            .catch(function(error){
                console.log('Found error: \n', error);
            });
            this.tclicked = !this.tclicked

        },
        getDiningCards:function(){
            fetch(this.server_url+"/cards/dining").then(function(response){
                response.json().then(function(data){
                    app.dcards = data;
                    console.log(data)
                    dclicked = true
                })
            })
            .catch(function(error){
                console.log('Found error: \n', error);
            });
            this.dclicked = !this.dclicked
        },
        getGroceryCards:function(){
            fetch(this.server_url+"/cards/grocery").then(function(response){
                response.json().then(function(data){
                    app.gcards = data;
                    console.log(data)
                })
            })
            .catch(function(error){
                console.log('Found error: \n', error);
            });
            this.gclicked = !this.gclicked
        },
        getGasCards:function(){
            fetch(this.server_url+"/cards/gas").then(function(response){
                response.json().then(function(data){
                    app.gascards = data;
                    console.log(data)
                })
            })
            .catch(function(error){
                console.log('Found error: \n', error);
            });
            this.gasclicked = !this.gasclicked
        },
        getShoppingCards:function(){
            fetch(this.server_url+"/cards/shopping").then(function(response){
                response.json().then(function(data){
                    app.scards = data;
                    console.log(data)
                })
            })
            .catch(function(error){
                console.log('Found error: \n', error);
            });
            this.sclicked = !this.sclicked
        }
    },
})
