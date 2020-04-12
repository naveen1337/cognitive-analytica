const mongoose = require('mongoose')

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

module.exports = mongoose.model('ca_scores', caschema); 