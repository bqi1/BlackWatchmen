const fs = require('fs'); // Import files system module

module.exports = {
	name: 'mission3',
	description: 'ROT13 Decryption.',
	execute(message, args) {
        if (args[0] === "start"){
            fs.readFile('./commands/intros/mission3.txt','utf8',function(err,contents){
                message.channel.send(contents);
            });
        } else if (args.join(" ").toLowerCase() === "at noon, the dealer will approach the designation."){
            message.channel.send("That is the correct answer. Well done!")
        } else {
            message.channel.send("That answer is incorrect.")
        }

	},
};