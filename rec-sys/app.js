const express = require('express')
const mongoose = require('mongoose')
const dotenv = require('dotenv').config()

const app = express()
const port = process.env.PORT | 5000

let url = process.env.DB_URI;

// DB Connection
mongoose.connect(process.env.DB_URI,
	{dbName:'ca_db',useNewUrlParser: true, useUnifiedTopology: true});
mongoose.set('useCreateIndex', true);

const db = mongoose.connection;
db.on('error', ()=>console.log("DB Connection Error"));
db.once('open',()=>console.log('Connction DB Done'));

// Schema for DB
const caschema = mongoose.Schema({
	name:{
		type:String,
		required:true,
	},

	similar:{
		type:Array,
		required:true,
	}
});

model = mongoose.model('ca_scores', caschema);

// Instance Information

app.route('/',(req,res)=>{
	res.json({
		Name: "Cognitive-Analytica",
		InstanceId : "7E3AL83Z",
		status : "Active"
	})
})

// returns a similar products, in the form of lower scror first in position  
app.get('/item/:productname',(req,res)=>{
	query = req.params.productname
	model.find({"name":query},(err,result)=>{
		if(err){
			res.json(err)
		}
		else{
			raw_data = result[0]['similar'][0]

			let sortable = [];
			for (let value of Object.keys(raw_data)) {
  				  sortable.push([value, raw_data[value]]);
				}
			similar = sortable.sort(function(a, b) {
	 			   return a[1] - b[1];
			});
			res.json({similar})
		}
	})
})

// listening 
app.listen(port,()=>{
	console.log(`Server Listening in ${port} `)
})