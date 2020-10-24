const job_channel = "767520496836673537"
module.exports = {
	name: 'apply',
	description: 'APPLY WITH US',
	execute(message, args) {

        if(message.channel.id === job_channel){
            message.reply("HEY. GLAD YOU WANT TO APPLY WITH US. UNFORTUNATELY WE ARE BOOKED WITH OUR 255 INTERNS. IT'S HARD ENOUGH FOR OUR BESTEST EMPLOYEE, MR. OGEN, TO KEEP TRACK OF THEIR NAMES AS IS. TRY APPLYING AFTER A FEW MONTHS :))))))))))");

        }else{
            message.reply("THIS ISN'T THE PLACE TO APPLY HAHAHAHAHA. TRY GOING TO THE JOB OPPORTUNITIES CHANNEL.")
        }

	},
};