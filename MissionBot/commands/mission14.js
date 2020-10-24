const fs = require('fs'); // Import files system module

module.exports = {
	name: 'mission14',
	description: 'bible',
	execute(message, args) {
        if (args[0] === "start"){
            fs.readFile('./commands/intros/mission14.txt','utf8',function(err,contents){
                message.channel.send(contents);
            });
        } else if (args.join(" ").toLowerCase() === "mcwhopper"){
            message.channel.send("That is the correct answer. Well done!")
        } else {
            message.channel.send("That answer is incorrect.")
        }

	},
};