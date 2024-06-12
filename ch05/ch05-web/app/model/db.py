
from sqlalchemy import  Column, ForeignKey, Integer, String, Date, Time, Sequence
from sqlalchemy.orm import relationship
from app.model.config import Base

class Login(Base):
   __tablename__ = 'login'
   id = Column(Integer, Sequence('login_id_seq', increment=1), primary_key = True)
   username = Column(String(45))
   password = Column(String(45))  
   
   member = relationship('Member', back_populates="login", uselist=False)

   def __init__(self, username, password, id = None):
      self.id = id
      self.username = username
      self.password = password
    
   def __repr__(self):
        return f"<Login {self.id} {self.username} {self.password} >"
     
   def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password
        }

class Member(Base):
   __tablename__ = 'member'
   id = Column(Integer, ForeignKey('login.id'), primary_key = True)
   firstname = Column(String(45), nullable=False)
   lastname = Column(String(45), nullable=False)  
   middlename = Column(String(45), nullable=False)
   email = Column(String(45), nullable=False)
   mobile = Column(String(45), nullable=False)
   role = Column(Integer, nullable=False)
   member_date = Column(Date, nullable=False)
   
   login = relationship('Login', back_populates="member")
   voter = relationship('Voter', back_populates="member", uselist=False)
   
   def __init__(self, id, firstname, lastname, middlename, email, mobile, role, member_date):
      self.id = id
      self.firstname = firstname
      self.lastname = lastname
      self.middlename = middlename
      self.email = email
      self.mobile = mobile
      self.member_date = member_date
      self.role = role
    
   def __repr__(self):
        return f"<Member {self.id} {self.firstname} {self.middlename} {self.lastname} {self.role}>"

   def to_json(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "lastname": self.lastname,
            "email": self.email,
            "mobile": self.mobile,
            "member_date": self.member_date,
            "role": self.role
        }

class Voter(Base):
    __tablename__ = 'voter'
    id = Column(Integer, Sequence('voter_id_seq', increment=1), primary_key = True)
    mid = Column(Integer, ForeignKey('member.id'), nullable=False, unique=True)
    voter_id = Column(String(45), nullable=False, unique=True)
    precinct = Column(String(45), nullable=False)
    last_vote_date = Column(Date, nullable=False)
    
    member = relationship('Member', back_populates="voter")
    votes = relationship('Vote', back_populates="voter")
    
    def __init__(self, mid, voter_id, precinct, last_vote_date, id = None):
      self.id = id
      self.mid = mid
      self.voter_id = voter_id
      self.precinct = precinct
      self.last_vote_date = last_vote_date
          
    def __repr__(self):
        return f"<Voter {self.id} {self.mid} {self.voter_id} {self.precinct} {self.last_vote_date}>"

    def to_json(self):
        return {
            "id": self.id,
            "mid": self.mid,
            "voter_id": self.voter_id,
            "precinct": self.precinct,
            "last_vote_date": self.last_vote_date
        }
    
class Election(Base):
    __tablename__ = 'election'
    id = Column(Integer, Sequence('election_id_seq', increment=1), primary_key = True)
    election_date = Column(Date, nullable=False)
    status = Column(String(10), nullable=False)
    total_voters = Column(Integer, nullable=False, default=0)
    
    
    candidates = relationship('Candidate', back_populates="election")
    votes = relationship('Vote', back_populates="election")
    vcounts = relationship('VoteCount', back_populates="election")
    
    def __init__(self, election_date, status, total_voters, id = None):
      self.id = id
      self.election_date = election_date
      self.status = status
      self.total_voters = total_voters
     
    def __repr__(self):
        return f"<Election {self.id} {self.election_date} {self.status} {self.total_voters}>"

    def to_json(self):
        return {
            "id": self.id,
            "election_date": self.election_date,
            "status": self.status,
            "total_voters": self.total_voters
        }
    
class Candidate(Base):
    __tablename__ = 'candidate'
    id = Column(Integer, Sequence('candidate_id_seq', increment=1), primary_key = True)
    elect_id = Column(Integer, ForeignKey('election.id'), nullable=False)
    cand_id = Column(String(20), nullable=False, unique=True)
    firstname = Column(String(45), nullable=False)
    lastname = Column(String(45), nullable=False)  
    middlename = Column(String(45), nullable=False) 
    address = Column(String(100), nullable=False) 
    tel = Column(String(20), nullable=False) 
    position = Column(String(45), nullable=False) 
    party = Column(String(100), nullable=False)
    filing_date = Column(Date, nullable=False)
    
    election = relationship('Election', back_populates="candidates")
    votes = relationship('Vote', back_populates="candidate")
    
    def __init__(self, elect_id, cand_id,firstname, lastname, middlename, address, tel, position, party, filing_date, id=None):
      self.id = id
      self.firstname = firstname
      self.lastname = lastname
      self.middlename = middlename
      self.elect_id = elect_id
      self.cand_id = cand_id
      self.address = address
      self.tel = tel
      self.position = position
      self.party = party
      self.filing_date = filing_date
      
    def __repr__(self):
        return f"<Candidate {self.id} {self.firstname} {self.middlename} {self.lastname} {self.elect_id} {self.position}>"

    def to_json(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "lastname": self.lastname,
            "elect_id": self.elect_id,
            "cand_id": self.cand_id,
            "address": self.address,
            "tel": self.tel,
            "position" : self.position,
            "party": self.party,
            "filing_date": self.filing_date
        }

class Vote(Base):
    __tablename__ = 'vote'
    id = Column(Integer, Sequence('vote_id_seq', increment=1), primary_key = True)
    voter_id = Column(String(45), ForeignKey('voter.voter_id'), nullable=False)
    election_id = Column(Integer, ForeignKey('election.id'), nullable=False)
    cand_id = Column(String(20), ForeignKey('candidate.cand_id'), nullable=False)
    vote_time = Column(Time(timezone=False), nullable=False)
    
    voter = relationship('Voter', back_populates="votes")
    election = relationship('Election', back_populates="votes")
    candidate = relationship('Candidate', back_populates="votes")
    
    def __init__(self, voter_id, election_id, cand_id, vote_time, id=None):
      self.id = id
      self.election_id = election_id
      self.cand_id = cand_id
      self.vote_time = vote_time
      self.voter_id = voter_id
            
    def __repr__(self):
        return f"<Vote {self.id} {self.voter_id} {self.election_id} {self.cand_id} {self.vote_time} >"

    def to_json(self):
        return {
            "id": self.id,
            "election_id": self.election_id,
            "voter_id": self.voter_id,
            "cand_id": self.cand_id,
            "vote_time": self.vote_time
        }
    
class VoteCount(Base):
    __tablename__ = 'vote_count'
    id = Column(Integer, Sequence('vote_count_id_seq', increment=1), primary_key = True)
    election_id = Column(Integer, ForeignKey('election.id'), nullable=False)
    precinct = Column(String(45),unique=True, nullable=False)
    final_tally =  Column(Integer, nullable=False)
    approved_date = Column(Date, nullable=False)
    
    election = relationship('Election', back_populates="vcounts")
    
    def __init__(self, election_id, precinct, final_tally, approved_date, id=None):
      self.id = id
      self.election_id = election_id
      self.precinct = precinct
      self.final_tally = final_tally
      self.approved_date = approved_date
      
    def __repr__(self):
        return f"<VoteCount {self.id} {self.election_id} {self.precinct} {self.final_tally} >"

    def to_json(self):
        return {
            "id": self.id,
            "election_id": self.election_id,
            "precinct": self.precinct,
            "final_tally": self.final_tally,
            "approved_date" : self.approved_date
        }