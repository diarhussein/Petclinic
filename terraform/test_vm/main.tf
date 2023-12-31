terraform {
  required_version = ">= 0.14"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.1.0"
    }
  }
}

variable "admin_username" {
  description = "The admin username for the VM"
}

variable "public_key_path" {
  description = "Path to the public SSH key to be used for the VM"
  default     = "~/.ssh/id_rsa.pub"
}

provider "azurerm" {
  features {}
  skip_provider_registration = true
}

# Use the existing Resource Group name and location
locals {
  resource_group_name = "diar_hussein-rg"
  location            = "West Europe" 
}

# Create a Storage Account
resource "azurerm_storage_account" "petclinic" {
  name                     = "petclinicsaccounttestvm"
  resource_group_name      = local.resource_group_name
  location                 = local.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  lifecycle {
    prevent_destroy = true
  }
}
# Create a Storage Container
resource "azurerm_storage_container" "petclinic" {
  name                  = "petclinicdevopstestvm"
  storage_account_name  = azurerm_storage_account.petclinic.name
  container_access_type = "private"
  lifecycle {
    prevent_destroy = true
  }
}
# Create a Virtual Network
resource "azurerm_virtual_network" "petclinic_vnet" {
  name                = "PetclinicVNettestVM"
  resource_group_name = local.resource_group_name
  location            = local.location
  address_space       = ["10.10.0.0/16"]
  lifecycle {
    prevent_destroy = true
  }
}

# Create a Subnet
resource "azurerm_subnet" "petclinic_subnet" {
  name                 = "PetclinicSubnettestVM"
  resource_group_name  = local.resource_group_name
  virtual_network_name = azurerm_virtual_network.petclinic_vnet.name
  address_prefixes     = ["10.10.0.0/24"]
  lifecycle {
    prevent_destroy = true
  }
}

# Create a Public IP Address
resource "azurerm_public_ip" "petclinic_public_ip" {
  name                = "PetclinicPublicIPtestVM"
  location            = local.location
  resource_group_name = local.resource_group_name
  allocation_method   = "Static"
  lifecycle {
    prevent_destroy = true
  }
}

# Create a Network Interface
resource "azurerm_network_interface" "petclinic_NIC" {
  name                = "PetclinicNICtestVM"
  location            = local.location
  resource_group_name = local.resource_group_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.petclinic_subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.petclinic_public_ip.id
  }
  lifecycle {
    prevent_destroy = true
  }
}

# Create a Virtual Machine
resource "azurerm_linux_virtual_machine" "petclinic_vm" {
  name                = "PetclinicVMtestVM"
  resource_group_name = local.resource_group_name
  location            = local.location
  size                = "Standard_DS1_v2"
  
  admin_username      = var.admin_username
  admin_ssh_key {
    username   = var.admin_username
    public_key = file(var.public_key_path)
  }
  
  network_interface_ids = [
    azurerm_network_interface.petclinic_NIC.id,
  ]

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Premium_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer = "0001-com-ubuntu-server-focal"
    sku = "20_04-lts-gen2"
    version   = "latest"
  }
}
