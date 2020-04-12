const express = require('express')
const mongoose = require('mongoose')
const dotenv = require('dotenv').config
const model = require('./model')

const app = express()
const port = process.env.PORT | 5000

var url = process.env.DB_URI;

// DB Connection
mongoose.connect(process.env.DB_URI,
	{dbName:'ca_db',useNewUrlParser: true, useUnifiedTopology: true});
mongoose.set('useCreateIndex', true);

const db = mongoose.connection;
db.on('error', ()=>console.log("DB Connection Error"));
db.once('open',()=>console.log('Connction DB Done'));



// Routes
app.route('/',(req,res)=>{
	res.json({
		Name: "Cognitive-Analytica",
		InstanceId : "7E3AL83Z",
		status : "Active"
	})
})

app.get('/item/:productname',(req,res)=>{
	query = req.params.productname
	model.find({"name":query},(err,result)=>{
		err ? res.json(err) : res.json(result)
	})
})

app.listen(port,()=>{
	console.log(`Server Listening in ${port} `)
})