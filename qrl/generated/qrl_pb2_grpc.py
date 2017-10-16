# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import qrl.generated.qrl_pb2 as qrl__pb2


class P2PNodeStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Ping = channel.unary_unary(
        '/qrl.P2PNode/Ping',
        request_serializer=qrl__pb2.PingReq.SerializeToString,
        response_deserializer=qrl__pb2.PongResp.FromString,
        )
    self.GetKnownPeers = channel.unary_unary(
        '/qrl.P2PNode/GetKnownPeers',
        request_serializer=qrl__pb2.GetKnownPeersReq.SerializeToString,
        response_deserializer=qrl__pb2.GetKnownPeersResp.FromString,
        )


class P2PNodeServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Ping(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetKnownPeers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_P2PNodeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=qrl__pb2.PingReq.FromString,
          response_serializer=qrl__pb2.PongResp.SerializeToString,
      ),
      'GetKnownPeers': grpc.unary_unary_rpc_method_handler(
          servicer.GetKnownPeers,
          request_deserializer=qrl__pb2.GetKnownPeersReq.FromString,
          response_serializer=qrl__pb2.GetKnownPeersResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'qrl.P2PNode', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class PublicAPIStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetKnownPeers = channel.unary_unary(
        '/qrl.PublicAPI/GetKnownPeers',
        request_serializer=qrl__pb2.GetKnownPeersReq.SerializeToString,
        response_deserializer=qrl__pb2.GetKnownPeersResp.FromString,
        )
    self.GetAddressStateLocal = channel.unary_unary(
        '/qrl.PublicAPI/GetAddressStateLocal',
        request_serializer=qrl__pb2.GetAddressStateLocalReq.SerializeToString,
        response_deserializer=qrl__pb2.GetAddressStateResp.FromString,
        )
    self.GetAddressState = channel.unary_unary(
        '/qrl.PublicAPI/GetAddressState',
        request_serializer=qrl__pb2.GetAddressStateReq.SerializeToString,
        response_deserializer=qrl__pb2.GetAddressStateResp.FromString,
        )
    self.TransferCoins = channel.unary_unary(
        '/qrl.PublicAPI/TransferCoins',
        request_serializer=qrl__pb2.TransferCoinsReq.SerializeToString,
        response_deserializer=qrl__pb2.TransferCoinsResp.FromString,
        )
    self.PushTransaction = channel.unary_unary(
        '/qrl.PublicAPI/PushTransaction',
        request_serializer=qrl__pb2.PushTransactionReq.SerializeToString,
        response_deserializer=qrl__pb2.PushTransactionReqResp.FromString,
        )


class PublicAPIServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetKnownPeers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAddressStateLocal(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAddressState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TransferCoins(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushTransaction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PublicAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetKnownPeers': grpc.unary_unary_rpc_method_handler(
          servicer.GetKnownPeers,
          request_deserializer=qrl__pb2.GetKnownPeersReq.FromString,
          response_serializer=qrl__pb2.GetKnownPeersResp.SerializeToString,
      ),
      'GetAddressStateLocal': grpc.unary_unary_rpc_method_handler(
          servicer.GetAddressStateLocal,
          request_deserializer=qrl__pb2.GetAddressStateLocalReq.FromString,
          response_serializer=qrl__pb2.GetAddressStateResp.SerializeToString,
      ),
      'GetAddressState': grpc.unary_unary_rpc_method_handler(
          servicer.GetAddressState,
          request_deserializer=qrl__pb2.GetAddressStateReq.FromString,
          response_serializer=qrl__pb2.GetAddressStateResp.SerializeToString,
      ),
      'TransferCoins': grpc.unary_unary_rpc_method_handler(
          servicer.TransferCoins,
          request_deserializer=qrl__pb2.TransferCoinsReq.FromString,
          response_serializer=qrl__pb2.TransferCoinsResp.SerializeToString,
      ),
      'PushTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.PushTransaction,
          request_deserializer=qrl__pb2.PushTransactionReq.FromString,
          response_serializer=qrl__pb2.PushTransactionReqResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'qrl.PublicAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))