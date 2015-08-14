# this script checks seats remaining for each crn in the crns array and sends me an email for each

require 'gmail'
require 'mechanize'

a = Mechanize.new
a.agent.http.verify_mode = OpenSSL::SSL::VERIFY_NONE

crns=[13115]
print "Seats Remaining:\n"
crns.each do |crn|
	seats_remaining = a.get("https://www.gosolar.gsu.edu/bprod/bwckschd.p_disp_detail_sched?term_in=201401&crn_in=#{crn}").search("//table[@summary='This layout table is used to present the seating numbers.']/tr[2]/td[3]/text()").to_s
  if seats_remaining.to_i > 0
		print "CRN "+crn.to_s+": "+seats_remaining.to_s+"\n"
		gmail = Gmail.connect('USER', 'PASS')
			gmail.deliver do
				to "EMAIL"
				subject "Class #{crn} is open!"
				body "CRN #{crn} has #{seats_remaining} seats available!\n"\
			       "https://paws.gsu.edu"
			end
		gmail.logout
  else
		print "Fail\n"
	end
end
