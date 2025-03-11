from flask import jsonify
from flask_jwt_extended import get_jwt_identity
import yfinance as yf
from app.modelos.ativo import Ativo

class CotacaoService:
    
    def get_cotation_yahoo(**ativos):
        try:    
            data = yf.download(list(ativos.keys()), period='1d', progress=False)['Close']
            return data.iloc[0][0] if (len(ativos.keys()) <= 1) else data
        except Exception as e:
            return f'erro {repr(e)}', 500
        
    def calc_rentabilidade(ativo_id):
        try:
            current_user_id = get_jwt_identity()
            ativo = Ativo.query.filter_by(id=ativo_id,user_id=current_user_id).first()
            
            if not ativo:
                return jsonify({'messagem': 'Ativo não encontrado', 'status': 'Erro'}), 404
            
            ativoKeys = {f'{ativo.codigo}.SA': float(ativo.preco)}
            ativo_preco_atual = CotacaoService.get_cotation_yahoo(**ativoKeys);
          
            rentabilidade = ((float(ativo_preco_atual) / float(ativo.preco)) -1)
            return jsonify({
                'ativo': ativo.to_json(),
                'preco_atual': f'{ativo_preco_atual:.2f}',
                'rentabilidade': f'{rentabilidade:.1%}'}), 200
        
        except Exception as e:
            return jsonify({
                'messagem': 'Erro ao calcular rentabilidade','status': 'Erro','msgErro': repr(e)}), 500
            
    def calc_carteira():
         current_user_id = get_jwt_identity()
         ativos = Ativo.query.filter_by(user_id=current_user_id).all()         
         
         if not ativos:
             return jsonify({'messagem': 'Carteira vazia', 'status': 'Erro'}), 404
         
         carteira = {}
         for c in ativos:
             c.codigo = c.codigo + '.SA'
             carteira[c.codigo] = float(c.preco)
        
         carteiraValor =  sum(carteira.values()) 
         
         cotation = CotacaoService.get_cotation_yahoo(**carteira) 
         
         carteira_atual = {}
         for c in cotation.columns:
             carteira_atual[c] = round(float(cotation[c].iloc[0]),2)
                      
         carteiraAtual = round(sum(carteira_atual.values()),2)
         
         rentabilidade = (carteiraAtual / carteiraValor) - 1
         
         myCarteira = {
                'carteira Valor': carteiraValor,
                'carteira Valor Atual': carteiraAtual,
                'rentabilidade': f'{rentabilidade:.1%}'
         }
         
         
         return jsonify(myCarteira), 200
         
        
            