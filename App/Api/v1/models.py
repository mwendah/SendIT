from app.api.v1 import  parcel
from flask_restful import Resource
from flask import response,jsonify,request


class ParcelModel(object):
	def _init_(self)
	self.db=ParcelModel()


	def create_order(self,destination,recipient,sender,weight,status)
	self.destination=destination
	self.recipient=recipient
	self.sender=sender
	self.weight=weight

	paylaod={

	"id":().int,
	"destination"=self.destination
	"recipient"=self.recipient
	"sender"=self.sender
	"weight"=self.weight
	"status"=self.status

	}

	parcel.parcels.append(payload)


	def get_all(self):
		return parcel.parcels



		def get_single_parcel(self,id):
	   for ParcelModel in parcel.parcels
:
				if ParcelModel["id"] ==id +1
				return ParcelModel


				def delete_order(self,id)
	self.id="id"

	paylaod={
	
	"id":().int,
	}

	parcel.parcels.delete(payload)

	def Create_Account(self,username,email,password)
	
self.username=username
	self.email=email
	self.password=password



	paylaod={

	"username"=self.email
	"email"=self.email
	"password"=self.password
	"

	}

	return jsonify{
	"message":"account created"

	}


			

