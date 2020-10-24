const fs = require('fs'); // Import files system module

module.exports = {
	name: 'mission1',
	description: 'The first mission involving simple reading of an image.',
	execute(message, args) {
        if (args[0] === "start"){
            fs.readFile('./commands/intros/mission1.txt','utf8',function(err,contents){
                message.channel.send(contents);
            });
        } else if (args.join(" ").toLowerCase() === "target located" || args.join(" ").toLowerCase() === "targetlocated"){
            message.channel.send("That is the correct answer. Well done!")
        } else {
            message.channel.send("That answer is incorrect.")
        }

	},
};