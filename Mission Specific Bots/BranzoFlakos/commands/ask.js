const ask_channel = "767518678438117408"
module.exports = {
	name: 'ask',
	description: 'APPLY WITH US',
	execute(message, args) {

        if(message.channel.id === ask_channel){
            message.reply("HEY. WE LOOOOOVE QUESTIONS. OUR SUPER FRIENDLY STAFF, JOE, WILL GET BACK TO YOU AS SOON AS POSSIBLE THROUGH THIS BOT, SO HANG TIGHT WITH YOUR CEREAL QUESTION!!!!!!!!!!");
            message.reply("Please refrain from directly messaging him unless you're an employee :))))")

        }else{
            message.reply("THIS ISN'T THE PLACE TO ASK QUESTIONS AHAHA. TRY GOING TO THE CUSTOMER INQUIRIES CHANNEL.")
        }

	},
};