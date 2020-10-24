const fs = require('fs'); // Import files system module

module.exports = {
	name: 'mission5',
	description: 'ROT18.',
	execute(message, args) {
        if (args[0] === "start"){
            fs.readFile('./commands/intros/mission5.txt','utf8',function(err,contents){
                message.channel.send(contents);
            });
        } else if (args.join(" ").toLowerCase() === "onlyadollarallsummer"){
            message.channel.send("That is the correct answer. Well done!")
        } else {
            message.channel.send("That answer is incorrect.")
        }

	},
};