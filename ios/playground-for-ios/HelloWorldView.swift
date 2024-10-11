//
//  ContentView.swift
//  playground-for-ios
//
//  Created by Jhonata on 20/01/24.
//

import SwiftUI

struct HelloWorldView: View {
    var body: some View {
        TabView {
            HomeView()
                .tabItem {
                    Image(systemName: "house")
                    Text("Início")
                }
            ProfileView()
                .tabItem {
                    Image(systemName: "person")
                    Text("Perfil")
                }
            SettingsView()
                .tabItem {
                    Image(systemName: "gear")
                    Text("Configurações")
                }
        }
        
    }
}

#Preview {
    HelloWorldView()
}
