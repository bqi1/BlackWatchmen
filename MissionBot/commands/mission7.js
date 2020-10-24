const fs = require('fs'); // Import files system module

module.exports = {
	name: 'mission7',
	description: 'pastebin',
	execute(message, args) {
        if (args[0] === "start"){
            fs.readFile('./commands/intros/mission7.txt','utf8',function(err,contents){
                message.channel.send(contents);
            });
        } else if ((args.join(" ").toLowerCase() === "hermetic order of the golden dawn")||(args.join(" ").toLowerCase() === "golden dawn")){
            message.channel.send("That is the correct answer. Well done!")
        } else {
            message.channel.send("That answer is incorrect.")
        }

	},
};