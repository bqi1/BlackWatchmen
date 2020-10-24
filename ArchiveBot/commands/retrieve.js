const fs = require('fs'); // Import files system module
const archiveFiles = fs.readdirSync('./commands/files');
let sepArchiveFiles = {};
for (const file of archiveFiles){
	var A = file.split(".");
	var filename = A[0];
	var extension = A[1];
	sepArchiveFiles[filename] = extension;
}
module.exports = {
	name: 'retrieve',
	description: 'Retrieves an image given single argument',
	execute(message, args) {
		if (args.length === 1){
			for (var key in sepArchiveFiles){
				if (args[0].toLowerCase() === key.toLowerCase()){
					message.channel.send({
						files: [{
							attachment: `./commands/files/${key}.`+sepArchiveFiles[key],
						}]
					})
					.catch (() => {
						message.reply("File does not exist in archives.");
					});
				}
			}
			
		} else{
			message.reply(`Invalid arguments.`);
		}
	},
};