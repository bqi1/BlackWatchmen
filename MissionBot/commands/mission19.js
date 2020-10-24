const fs = require('fs'); // Import files system module

module.exports = {
	name: 'mission19',
	description: 'Norweigan Decipher.',
	execute(message, args) {
        if (args[0] === "start"){
            fs.readFile('./commands/intros/mission19.txt','utf8',function(err,contents){
                message.channel.send(contents);
            });
        } else if (args.join(" ").toLowerCase() === "439543"){
            message.channel.send("That is the correct answer. Well done!")
        } else {
            message.channel.send("That answer is incorrect.")
        }

	},
};