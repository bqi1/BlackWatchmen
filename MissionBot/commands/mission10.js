const fs = require('fs'); // Import files system module

module.exports = {
	name: 'mission10',
	description: 'paintlmao',
	execute(message, args) {
        if (args[0] === "start"){
            fs.readFile('./commands/intros/mission10.txt','utf8',function(err,contents){
                message.channel.send(contents);
            });
        } else if (args.join(" ").toLowerCase() === "the device will detonate at kingsway at 0800"){
            message.channel.send("That is the correct answer. Well done!")
        } else {
            message.channel.send("That answer is incorrect.")
        }

	},
};