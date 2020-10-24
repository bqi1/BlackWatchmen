const fs = require('fs'); // Import files system module

module.exports = {
	name: 'mission2',
	description: 'Audio translation.',
	execute(message, args) {
        if (args[0] === "start"){
            fs.readFile('./commands/intros/mission2.txt','utf8',function(err,contents){
                message.channel.send(contents);
            });
        } else if (args.join(" ").toLowerCase() === "do not trust him. he is a double agent."){
            message.channel.send("That is the correct answer. Well done!")
        } else {
            message.channel.send("That answer is incorrect.")
        }

	},
};